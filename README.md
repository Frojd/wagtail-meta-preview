![wagtail-meta-preview](https://github.com/rinti/wagtail-meta-preview/workflows/wagtail-meta-preview/badge.svg)
[![PyPI version](https://badge.fury.io/py/wagtail-meta-preview.svg)](https://badge.fury.io/py/wagtail-meta-preview)

# wagtail meta preview

## Current supported versions

Wagtail Meta Preview requires Wagtail 4.1+

## Preview

Wagtail Meta Preview provides panels for previewing Facebook sharing, Twitter sharing and Google search results in the Wagtail admin.
Example of how the Facebook share looks like:

![example-facebook-preview](https://raw.githubusercontent.com/rinti/wagtail-meta-preview/master/docs/img/facebook-preview-example.PNG)

## Documentation

- [Getting started](./docs/1-getting-started.md)
- [Setting up panels](./docs/2-setting-up-panels.md)
- [Settings](./docs/3-settings.md)

## Development

### Dev server

The easiest way is to clone this repo, cd into it and just `docker-compose up`, this should
start a server on http://localhost:8123/admin/ (user: admin, pw: admin) with a couple of page types to test with.

### Running tests

`docker-compose exec web python runtests.py`


## License

Wagtail Meta Preview is released under the [MIT License](http://www.opensource.org/licenses/MIT).
