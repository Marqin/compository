"""
    Copyright (c) 2016 Hubert Jarosz. All rights reserved.
    Licensed under the MIT license. See LICENSE file in the project root for full license information.
"""

repo_dir = "/path/to/zip/packages/directory/"
repo_url = "http://example.com/"
pkg_name = "package/name"

try:
    import pathlib
except ImportError:
    import sys
    if sys.version_info[:2] < (3, 4):
        raise Exception("This software needs Python 3.4 or newer!")
    else:
        raise

import zipfile
import json

def generator(pkgs):
    for pkg in pkgs:
        try:
            archive = zipfile.ZipFile(str(pkg), "r")
            composer_json = archive.read("composer.json").decode("UTF-8")
            composer = json.loads(composer_json)

            version = str(pkg.stem).split("-")[-1]
            composer["version"] = version
            composer["dist"] = {
                "type": "zip",
                "url": repo_url + "/" + pkg.name
            }

            yield (version, composer)
        except:
            continue

path = pathlib.Path(repo_dir).resolve()
pkgs = [x for x in path.iterdir() if x.is_file() and x.suffix == ".zip"]

repo = {"packages":{pkg_name: dict(generator(pkgs))}}

try:
    fp = (path / "packages.json").open("w")
    dump = json.dumps(repo)
    fp.write(dump+"\n")
    fp.close()
except:
    raise
