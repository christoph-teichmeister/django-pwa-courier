const offlineFile = "/offline/"

// Using CACHE_VERSION from the Django template context (git commit hash)
const staticCacheName = `{{ PWA_MANIFEST_ID }}-cache-v{{ PWA_CACHE_VERSION|default:'1.0.0' }}`;

const criticalFilesToCache = [
  // TODO CT: Create offline file
  // 'offlineFile',
  '/static/images/favicons/favicon.ico', // Universal fallback
  '/static/images/favicons/android/android-launchericon-192-192.png', // PWA standard
  '/static/images/favicons/ios/180.png' // Most common iOS size
];

const nonCriticalFavicons = [
  '/static/images/favicons/windows11/SmallTile.scale-100.png',
  '/static/images/favicons/windows11/SmallTile.scale-125.png',
  '/static/images/favicons/windows11/SmallTile.scale-150.png',
  '/static/images/favicons/windows11/SmallTile.scale-200.png',
  '/static/images/favicons/windows11/SmallTile.scale-400.png',
  '/static/images/favicons/windows11/Square150x150Logo.scale-100.png',
  '/static/images/favicons/windows11/Square150x150Logo.scale-125.png',
  '/static/images/favicons/windows11/Square150x150Logo.scale-150.png',
  '/static/images/favicons/windows11/Square150x150Logo.scale-200.png',
  '/static/images/favicons/windows11/Square150x150Logo.scale-400.png',
  '/static/images/favicons/windows11/Wide310x150Logo.scale-100.png',
  '/static/images/favicons/windows11/Wide310x150Logo.scale-125.png',
  '/static/images/favicons/windows11/Wide310x150Logo.scale-150.png',
  '/static/images/favicons/windows11/Wide310x150Logo.scale-200.png',
  '/static/images/favicons/windows11/Wide310x150Logo.scale-400.png',
  '/static/images/favicons/windows11/LargeTile.scale-100.png',
  '/static/images/favicons/windows11/LargeTile.scale-125.png',
  '/static/images/favicons/windows11/LargeTile.scale-150.png',
  '/static/images/favicons/windows11/LargeTile.scale-200.png',
  '/static/images/favicons/windows11/LargeTile.scale-400.png',
  '/static/images/favicons/windows11/Square44x44Logo.scale-100.png',
  '/static/images/favicons/windows11/Square44x44Logo.scale-125.png',
  '/static/images/favicons/windows11/Square44x44Logo.scale-150.png',
  '/static/images/favicons/windows11/Square44x44Logo.scale-200.png',
  '/static/images/favicons/windows11/Square44x44Logo.scale-400.png',
  '/static/images/favicons/windows11/StoreLogo.scale-100.png',
  '/static/images/favicons/windows11/StoreLogo.scale-125.png',
  '/static/images/favicons/windows11/StoreLogo.scale-150.png',
  '/static/images/favicons/windows11/StoreLogo.scale-200.png',
  '/static/images/favicons/windows11/StoreLogo.scale-400.png',
  '/static/images/favicons/windows11/SplashScreen.scale-100.png',
  '/static/images/favicons/windows11/SplashScreen.scale-125.png',
  '/static/images/favicons/windows11/SplashScreen.scale-150.png',
  '/static/images/favicons/windows11/SplashScreen.scale-200.png',
  '/static/images/favicons/windows11/SplashScreen.scale-400.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-16.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-20.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-24.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-30.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-32.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-36.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-40.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-44.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-48.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-60.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-64.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-72.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-80.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-96.png',
  '/static/images/favicons/windows11/Square44x44Logo.targetsize-256.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-16.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-20.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-24.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-30.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-32.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-36.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-40.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-44.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-48.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-60.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-64.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-72.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-80.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-96.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-unplated_targetsize-256.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-16.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-20.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-24.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-30.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-32.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-36.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-40.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-44.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-48.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-60.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-64.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-72.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-80.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-96.png',
  '/static/images/favicons/windows11/Square44x44Logo.altform-lightunplated_targetsize-256.png',
  '/static/images/favicons/android/android-launchericon-512-512.png',
  '/static/images/favicons/android/android-launchericon-144-144.png',
  '/static/images/favicons/android/android-launchericon-96-96.png',
  '/static/images/favicons/android/android-launchericon-72-72.png',
  '/static/images/favicons/android/android-launchericon-48-48.png',
  '/static/images/favicons/ios/16.png',
  '/static/images/favicons/ios/20.png',
  '/static/images/favicons/ios/29.png',
  '/static/images/favicons/ios/32.png',
  '/static/images/favicons/ios/40.png',
  '/static/images/favicons/ios/50.png',
  '/static/images/favicons/ios/57.png',
  '/static/images/favicons/ios/58.png',
  '/static/images/favicons/ios/60.png',
  '/static/images/favicons/ios/64.png',
  '/static/images/favicons/ios/72.png',
  '/static/images/favicons/ios/76.png',
  '/static/images/favicons/ios/80.png',
  '/static/images/favicons/ios/87.png',
  '/static/images/favicons/ios/100.png',
  '/static/images/favicons/ios/114.png',
  '/static/images/favicons/ios/120.png',
  '/static/images/favicons/ios/128.png',
  '/static/images/favicons/ios/144.png',
  '/static/images/favicons/ios/152.png',
  '/static/images/favicons/ios/167.png',
  '/static/images/favicons/ios/192.png',
  '/static/images/favicons/ios/256.png',
  '/static/images/favicons/ios/512.png',
  '/static/images/favicons/ios/1024.png'
  // TODO CT: Add splash images here
]

// Cache on installation
self.addEventListener("install", event => {
  this.skipWaiting();

  event.waitUntil(
    caches.open(staticCacheName)
      .then(cache => {
        return Promise.allSettled(
          criticalFilesToCache.map(file =>
            cache.add(file).catch(err =>
              console.warn(`Failed to cache ${file}:`, err)
            )
          )
        );
      })
  );
});

// Clear cache on activating
self.addEventListener('activate', event => {
  self.clients.claim(); // Take control of all clients immediately

  event.waitUntil(caches.keys().then(cacheNames => {
    return Promise.all(cacheNames
      .filter(cacheName => (cacheName.startsWith("{{ PWA_MANIFEST_ID" +
        " }}-cache-")))
      .filter(cacheName => (cacheName !== staticCacheName))
      .map(cacheName => caches.delete(cacheName)));
  }));
});

// Serve from Cache
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);

  // Different strategies for different content types
  if (url.pathname.startsWith('/api/')) {
    // Network first for API calls
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (response.ok) {
            const responseClone = response.clone();
            caches.open(staticCacheName).then(cache => {
              cache.put(event.request, responseClone);
            });
          }
          return response;
        })
        .catch(() => caches.match(event.request))
    );
  } else if (url.pathname.startsWith('/static/')) {
    // Cache first for static assets, but also cache new resources
    event.respondWith(
      caches.match(event.request)
        .then(response => {
          if (response) {
            return response;
          }

          // If not in cache, fetch from the network and cache it
          return fetch(event.request)
            .then(networkResponse => {
              if (networkResponse.ok) {
                const responseClone = networkResponse.clone();
                caches.open(staticCacheName).then(cache => {
                  cache.put(event.request, responseClone);
                });
              }
              return networkResponse;
            });
        })
    );
  } else if (url.pathname.includes('/favicons/')) {
    // Check if it's a favicon request
    event.respondWith(
      caches.match(event.request)
        .then(cachedResponse => {
          if (cachedResponse) {
            return cachedResponse;
          }

          // Check if this is a non-critical favicon
          const isNonCritical = nonCriticalFavicons.some(favicon =>
            url.pathname.includes(favicon.split('/').pop())
          );

          if (isNonCritical) {
            // Lazy load: fetch and cache on first request
            return fetch(event.request)
              .then(response => {
                if (response.ok) {
                  const responseClone = response.clone();
                  caches.open(staticCacheName).then(cache => {
                    cache.put(event.request, responseClone);
                  });
                }
                return response;
              })
              .catch(() => {
                // Fallback to the main favicon if a specific one fails
                return caches.match('/static/images/favicons/favicon.ico');
              });
          } else {
            // For other favicon requests, try to fetch
            return fetch(event.request);
          }

        })
    );
  } else {
    // Network first for HTML pages
    event.respondWith(
      fetch(event.request)
        .catch(() => caches.match(event.request))
        .catch(() => caches.match(offlineFile))
    );
  }
});

// Register an event listener for the 'push' event.
self.addEventListener('push', (event) => {
  // Retrieve the textual payload from event.data (a PushMessageData object).
  // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
  // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
  const {head, ...options} = JSON.parse(event.data.text());

  // Keep the service worker alive until the notification is created.
  event.waitUntil(self.registration.showNotification(head, options));
});

// Function to get the URL for a specific action from a list of actionClickUrls
const getURLForAction = (action, actionClickUrls) => {
  for (const clickUrl of actionClickUrls) {
    if (clickUrl.action === action) {
      return clickUrl.url;
    }
  }
  // If no match is found, you may choose to return null or some other default value.
  return null;
};

// Function to navigate the client to a URL, handling different scenarios
const navigateClientToUrl = (event, url) => event.waitUntil(
    clients.matchAll({includeUncontrolled: true})
      .then(clientsArray => {
          // Filter out clients with URLs containing /{{ ADMIN_URL }}/
          const filteredClients = clientsArray.filter(client => !client.url.includes(`/{{ ADMIN_URL }}`));

          if (filteredClients.length > 0) {
            return filteredClients[0].focus().then(function (client) {
              client.postMessage({
                action: 'redirect-from-notificationclick',
                url: url,
              });
            })
          } else {
            // If no clients are available, open a new window
            return clients.openWindow(url);
          }
        }
      )
  )
;

// Event listener for the 'notificationclick' event
self.addEventListener('notificationclick', function (event) {
  // Close the notification popout
  event.notification.close();

  // Extract relevant data from the notification
  const {actionClickUrls, notificationClickUrl} = event.notification.data;

  // Check if an action was clicked
  if (!event.action) {
    // If no specific action was clicked,
    // navigate to the default notificationClickUrl
    navigateClientToUrl(event, notificationClickUrl);
    return;
  }

  // Handle different actions
  switch (event.action) {
    case 'click-me-action':
      // For the 'click-me-action', navigate to the corresponding URL
      navigateClientToUrl(event, getURLForAction('click-me-action', actionClickUrls));
      break;
    default:
      // Log unknown actions to the console
      console.log(`Unknown action clicked: '${event.action}'`);
      break;
  }
});
