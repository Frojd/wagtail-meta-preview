# Changelog

## [Unreleased]
### Added
### Changed
### Fixed
### Removed

## [4.2.1] - 2025-03-14
### Changed
- Raise console warning if admin page field is missing #16 (@marteinn)

### Fixed
- Make sure html chracters are decoded in BaseSettings.get_title()/get_description() #17 (@marteinn)
- Make sure drafttail field content are read as plaintext #18 (@marteinn)


## [4.2.0] - 2025-02-26
### Added
- Add python 3.13 support (@marteinn)
- Add support for serving default image in preview panel (@marteinn)

### Changed
- Improve developement instructions (@marteinn)
- Make sure title and descriptions are truncated if too long (@marteinn)
- Strip html tags from preview widget (@marteinn)
- Strip html tags from get_title/get_description in settings (@marteinn)

### Fixed
- Fix broken image preview #12 (@marteinn)
- Drop deprecated version from docker-compose (@marteinn)
- Upgrade postgres image for development (@marteinn)
- Upgrade development version of python to 3.10 (@marteinn)
- Make sure test app can properly load templates (@marteinn)
- Fix bug in twitter panel where it used facebook settings (@marteinn)

### Removed
- Drop support for EOL python 3.8 (@marteinn)
- Drop support for EOL Wagtail 6.0 (@marteinn)

## [4.1.0] - 2024-02-19
### Added
- Add Wagtail 6.0 support (@marteinn)

### Removed
- Drop support for EOL Wagtail 4.1 (@marteinn)


## [4.0.0] - 2023-12-29
### Added
- Add python 3.12 support (@marteinn)
- Add Wagtail 5.2 support (@marteinn)

### Fixed
- Upgrade github actions

### Removed
- Drop support for EOL Python 3.7 (@marteinn)
- Drop support for EOL Wagtail 5.1 (@marteinn)


## [3.0.0] - 2023-06-15
### Fixed
- Fix issue with meta preview input field not being rendered
- Drop redundant section legend in preview
- Fix issue with meta preview descriptions not showing in dark mode

### Removed
- Drop support for Wagtail<4.1

## [2.0.1] - 2023-05-21
### Added
- Add Wagtail 5.0 support
- Add changelog

### Changed
- Move project to Frojd organization

### Fixed
- Refactor github actions
- Add white background to preview boxes (@marteinn)

### Removed
- Drop unused settings META_PREVIEW_TWITTER_TITLE_FALLBACK and META_PREVIEW_TWITTER_IMAGE_FALLBACK

## [2.0.0] - 2023-05-03
### Added
- Add Wagtail 4.0 support

### Removed
- Remove Wagtail 3 support
- Drop python 3.6 support

## [1.1.2] - 2022-05-18
### Fixed
- Fix invalid package version

## [1.1.1] - 2022-05-18
### Fixed
- Drop invalid classifier

## [1.1.0] - 2022-05-18
### Added
- Add Wagtail 3.0 compatibility

### Fixed
- Add pypy badge to readme
- Add url meta and framework classifiers
- Add release CI action

## [1.0.3] - 2022-08-02
### Fixed
- Fix bug where default titles didn't get set correctly
- Fix admin url in js

## [1.0.1] - 2020-08-02
### Fixed
- Update project manifest
- Rename admin css/js files
- Add screenshot example in readme

## [1.0.0] - 2020-08-02
### Added
- Initial release
