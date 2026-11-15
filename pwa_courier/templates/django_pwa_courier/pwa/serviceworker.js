{% load static %}// django-pwa-courier service worker. Extend it in your own template:
//   {% templatetag openblock %} extends "django_pwa_courier/pwa/serviceworker.js" {% templatetag closeblock %}
// and point PWA_SERVICE_WORKER_TEMPLATE at it. Override `fetch` to replace the caching, append to `extra`.
const cachePrefix = "{{ PWA_CACHE_PREFIX|escapejs }}";
const staticCacheName = `${cachePrefix}v{{ PWA_CACHE_VERSION|escapejs }}`;
const offlineUrl = "{% url 'pwa_courier:offline' %}";
const staticUrl = "{% get_static_prefix %}";

const filesToPrecache = [
  offlineUrl,
  {% for icon in PWA_MANIFEST.icons %}"{{ icon.src|escapejs }}",
  {% endfor %}{% block precache %}{% endblock %}
];

self.addEventListener("install", event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(staticCacheName).then(cache => Promise.allSettled(
      filesToPrecache.map(file => cache.add(file).catch(err => console.warn(`Failed to cache ${file}:`, err)))
    ))
  );
});

self.addEventListener("activate", event => {
  self.clients.claim();
  event.waitUntil(caches.keys().then(names => Promise.all(names
    .filter(name => name.startsWith(cachePrefix) && name !== staticCacheName)
    .map(name => caches.delete(name)))));
});

{% block fetch %}
const putInCache = (request, response) => {
  if (response.ok) {
    const clone = response.clone();
    caches.open(staticCacheName).then(cache => cache.put(request, clone));
  }
  return response;
};

self.addEventListener("fetch", event => {
  const request = event.request;
  const url = new URL(request.url);
  if (request.method !== "GET" || url.origin !== self.location.origin) {
    return;
  }

  if (request.mode === "navigate") {
    // Pages: network first, then the cached copy, then the offline page
    event.respondWith(
      fetch(request)
        .catch(() => caches.match(request).then(cached => cached || caches.match(offlineUrl)))
    );
  } else if (url.pathname.startsWith(staticUrl)) {
    // Static files: cache first, cache what is fetched
    event.respondWith(
      caches.match(request).then(cached => cached || fetch(request).then(response => putInCache(request, response)))
    );
  }
});
{% endblock fetch %}

self.addEventListener("push", event => {
  const {head, ...options} = JSON.parse(event.data.text());
  // Keep the worker alive until the notification is shown (iOS drops the subscription otherwise)
  event.waitUntil(self.registration.showNotification(head, options));
});

// Focus an open app window and let the page redirect itself (works on iOS home-screen apps), else open a new one
const openUrl = (event, url) => event.waitUntil(
  clients.matchAll({type: "window", includeUncontrolled: true}).then(clientList => {
    const adminUrl = "{{ PWA_ADMIN_URL|escapejs }}";
    const appClients = clientList.filter(client => !adminUrl || !new URL(client.url).pathname.startsWith(adminUrl));
    if (appClients.length > 0) {
      return appClients[0].focus().then(client => client.postMessage({action: "redirect-from-notificationclick", url}));
    }
    return clients.openWindow(url);
  })
);

self.addEventListener("notificationclick", event => {
  event.notification.close();
  const {actionClickUrls = [], notificationClickUrl} = event.notification.data || {};
  const actionUrl = event.action && (actionClickUrls.find(item => item.action === event.action) || {}).url;
  openUrl(event, actionUrl || notificationClickUrl || "/");
});

{% block extra %}{% endblock %}
