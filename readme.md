## Getting Started

* The Harvard Crimson Comp Website is a static site that is generated using jinja2. It is hosted out of an S3 bucket on AWS. So in order to make modifications to the site and to deploy it to S3, you need to ensure that you are operating on a **Python 3** environment that has jinja2 installed. You also need to have the latest version of `ruby` installed alongside the latest version of `gem` (the package manager for Ruby).

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
* In the home directory, run `./template.py`. This generates static files that are stored in the **./rendered/** directory.

* `cd` into the **rendered** directory and run `python -m http.server`. You can now visit <http://localhost:8000> to view the website. This command will not work in Python 2.

* Note: you will have to re-run `./template.py` in the repo's home directory in order to regenerate the static files. They will not be automatically updated.

## Deployment
* Once you're ready to deploy the site, run `./template.py` to generate the **rendered/** directory. The files in this folder are the ones that S3 actually hosts.

* The `s3_website` gem should already be installed as a result of the `bundle install` command above, but if it isn't then install it using `gem install s3_website`.

* `bundle exec s3_website cfg create` creates a new s3_website.yml file. Put in your AWS credentials (same as with the normal website) and `comp.thecrimson.com` as the bucket. Additionally add a line that says `site: rendered/`. s3\_website.yml is set up to be ignored by git, and it will not be pushed to the S3 bucket during the deployment.

* `bundle exec s3_website cfg apply` configures everything for you.

* `bundle exec s3_website push` deploys the code to the website. If prompted to use CloudFront, say yes. If you've already configured s3_website, then you can can skip directly to this step after running `./template.py`.

* Check <http://comp.thecrimson.com> to verify that the site has been updated!
