## Getting Started

* The Harvard Crimson Comp Website is a static site that is generated using Jekyll. It is deployed with GitHub Pages. To make modifications to the site, you will need `ruby` installed and the latest version of `gem`.

* Make sure that you've already `git clone`d this repo to your computer and are currently in the home directory of the repo.

* Once you've installed Ruby and ensured that you have the repo locally, add these two lines to the bottom of your `~/.bashrc` to ensure that every gem is stored in a local directory.
    ```
    export GEM_HOME=~/.gem
    export GEM_PATH=~/.gem
    ```

* Once you've done this, run the following commands:
    - `source ~/.bashrc` (enables the environment variables set above)
    - `gem install bundler` (install a gem that helps with package management)
    - `bundle install` (installs all the required gems)

* If any gem in particular gives you trouble during the `bundle install` process, you can try installing it directly with `gem install [gemname]`.

## Development
* In the home directory, run `bundle exec jekyll serve`. This will start a local development server.

* The default port is `4000` so visit `http://localhost:4000` to see the site!

* Any changes to CSS or HTML files will automatically trigger a rebuild, so no need to restart the server.

* If you update the information in `_config.yml`, you _will_ need to restart the server.

## Deployment
* Since this website is hosted with GitHub Pages, you simply need to commit and push your changes to the `master` branch. This will automatically start a build process (note: this is only because GitHub Pages has automatic support for Jekyll).

* Wait about a minute and check <https://comp.thecrimson.com> to verify the site has been updated!