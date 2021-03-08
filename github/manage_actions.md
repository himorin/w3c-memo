# On managing CI for repositories

Goals and considerations

* Collect configuration requirements and examples, including to understand necessity options
* Provide best practice(s) of CI configuration, with minimized efforts to keep updated
  * Provide up-to-date set of configuration files and instructions to [repository manager](https://github.com/w3c/ash-nazg), for respec and bikeshed
    * CI could be used for various targets, not just gh-pages or publishing. These could also be included.
    * Also consider possibility of automatic update (filing PRs)
* Collect and provide FAQ on CI configurations and issues detected, including ones not put into repository manager


## List of use cases

### For specs using respec

[respec](https://respec.org/docs/) is JavaScript based processing tool and run within web browsers as post-process on 'onLoad', 
and does not require CI for showing drafts. 

* Usually, GitHub repository is onfigured to have the same branch as default and source of github pages.
* For `/TR/`, processing static output is reuiqred. Export using menu button added by respec, or [spec generator](https://labs.w3.org/spec-generator/) is used.
  * [echidna](https://labs.w3.org/echidna/) calls spec generator for generation
* CI is used for updating `/TR/` follwoing events like PR merged to the default branch (e.g. [did-core repository](https://github.com/w3c/did-core/blob/main/.travis.yml))

### For specs using bikeshed

[bikeshed](https://tabatkins.github.io/bikeshed/) is a converter of document format, and conversion is required to get HTML document 
for preview etc.

* Usually, CI is configured to generate HTML for github pages, which is the same one as in `/TR/`.
* CSSWG provides [web API for bikeshed processing](https://api.csswg.org/bikeshed/), which is widely used for CI via curl.
  * The web API is reported [to fail sometimes](https://github.com/immersive-web/depth-sensing/pull/17#issuecomment-777865853)
* bikeshed uses references of WebIDL in specs, and needs to be updated to the newest data set for processing using local installation


## Configuration examples

* GitHub Actions
  * Place action configuration files into `.github/workflows/`, like [deploy.yml for IWWG/webxr](https://github.com/immersive-web/webxr/blob/main/.github/workflows/deploy.yml)
  * Additionally required non-file based configurations
    * No additional configuration is required for github pages.
    * Key required for echidna publishing to `/TR/`
  * W3C customized action [spec-prod](https://github.com/w3c/spec-prod/)
* TravisCI
  * Place CI configuration file as `.travis.yml`, like [.travis.yml for did-code](https://github.com/w3c/did-core/blob/main/.travis.yml)
  * Additionally required non-file based configurations
    * Deploy key is required for github pages. 
    * Key required for echidna publishing to `/TR/`

### For respec

* did-core has [.travis.yml](https://github.com/w3c/did-core/blob/main/.travis.yml) for publishing to `/TR/` using echidna on every update to `main`
* [mediacapture-main](https://github.com/w3c/mediacapture-main/tree/main/.github/workflows) uses several workflows for validate, publish, and tidy

### For bikeshed

* [IWWG/IWCG](https://github.com/immersive-web/webxr/blob/main/.github/workflows/deploy.yml) is using the same workflow (of GitHub Actions) over all repositories
* [WebAuthn](https://github.com/w3c/webauthn/blob/master/.travis.yml) installes bikeshed and build spec, with option to use cached copy of bikeshed data in git repository
* [webtransport](https://github.com/w3c/webtransport/blob/main/.github/workflows/pr-push.yml) uses w3c/spec-prod action
