# compository

Simple Python script that turns directory with [Composer](https://github.com/composer/composer) zip packages into Composer repository.

It can be used as a workaround for [composer/composer#2391](https://github.com/composer/composer/issues/2391).

## Requirements
* Python 3.4 or newer

## Usage

Set variables `repo_dir`, `repo_url` and `pkg_name` (those at the beggining of program) and run it periodically with cron (or some other scheduler).
