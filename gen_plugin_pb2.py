#!/usr/bin/env python
# -*- coding: utf-8 -*-

import google.protobuf
import os
from distutils.spawn import find_executable
import subprocess
import sys


def gen_plugin_pb2(pb_dir):
    pkgdir = os.path.dirname(google.protobuf.__file__)
    outputdir = os.path.join(pkgdir, "compiler")
    os.makedirs(outputdir)
    open(os.path.join(outputdir, "__init__.py"), "w+").close()
    protoc = find_executable('protoc')
    subprocess.call(
        [protoc, "-I" + os.path.join(pb_dir, "src"),
         "--python_out=" + os.path.join(pkgdir, "../../"),
         os.path.join(pb_dir, "src/google/protobuf/compiler/plugin.proto")])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write("gen_plugin_pb2.py <protubuf project dir>\n")
        sys.exit(1)
    gen_plugin_pb2(os.path.expanduser(sys.argv[1]))
