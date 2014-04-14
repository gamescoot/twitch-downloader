#!/usr/bin/env python
import sys, json
from subprocess import call

call(["git","commit","-a","-m","'hello'"])
call(["ls"])