from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import (
    DEPLOYMENT_STATUS_BETA,
    DEV_DEPENDENCIES,
    LICENSE_MIT,
    SUPPORTED_DJANGO_VERSIONS,
)
from ambient_package_update.metadata.maintainer import PackageMaintainer
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent

METADATA = PackageMetadata(
    module_name="pwa_courier",
    package_name="django-pwa-courier",
    github_package_group="christoph-teichmeister",
    authors=[
        PackageAuthor(
            name="Chris Teichmeister",
            email="christoph.teichmeister@gmail.com",
        ),
    ],
    maintainer=PackageMaintainer(
        name="Chris Teichmeister",
        url="https://chris.teichmeister.lu/",
        email="christoph.teichmeister@gmail.com",
    ),
    licenser="Chris Teichmeister",
    license=LICENSE_MIT,
    license_year=2025,
    development_status=DEPLOYMENT_STATUS_BETA,
    has_migrations=False,
    readme_content=ReadmeContent(uses_internationalisation=False),
    dependencies=[
        f"Django>={SUPPORTED_DJANGO_VERSIONS[0]}",
        "pywebpush>=2",
    ],
    tests_require_django=False,  # TODO CT: Remove this
    supported_django_versions=SUPPORTED_DJANGO_VERSIONS,
    supported_python_versions=[
        "3.10",
        "3.11",
        "3.12",
        "3.13",
    ],
    optional_dependencies={
        "dev": [*DEV_DEPENDENCIES],
    },
    ruff_ignore_list=[],
)
