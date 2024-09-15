# Define the version components
major_version = 1
minor_version = 0
patch_version = 0

pre_release = 'alpha'  # Can be 'alpha', 'beta', 'rc', etc.
# pre_release = None  # Can be 'alpha', 'beta', 'rc', etc.
build_metadata = '001'  # Can be build number, date, or other identifier

# Define the version label
version_label = 'v'

if pre_release:
    __version__ = f'{version_label}{major_version}.{minor_version}.{patch_version}-{pre_release}+{build_metadata}'
else:
    __version__ = f'{version_label}{major_version}.{minor_version}.{patch_version}'


def get_version():
    return __version__

print(get_version())