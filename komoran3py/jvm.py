# -*- coding: utf-8 -*-

import os
import sys
import jpype

def get_default_jvm_path():
    return jpype.getDefaultJVMPath()

def init_jvm(jvmpath=None, libraries=None, max_heap=1024):
    """Initializes the Java virtual machine (JVM).
    use Java in jpype.getDefaultJVMPath
    """

    if jpype.isJVMStarted():
        return None

    if not libraries:
        installpath = os.path.dirname(os.path.realpath(__file__))
        libpaths = [
            '{0}',
            '{0}{1}bin',
            '{0}{1}aho-corasick.jar',
            '{0}{1}shineware-common-1.0.jar',
            '{0}{1}shineware-ds-1.0.jar',
            '{0}{1}komoran-3.0.jar',
            '{0}{1}*'
        ]
        javadir = '%s%sjava' % (installpath, os.sep)

    args = [javadir, os.sep]
    libpaths = [p.format(*args) for p in libpaths]
    classpath = os.pathsep.join(libpaths)
    if jvmpath is None:
        jvmpath = jpype.getDefaultJVMPath()

    try:
        jpype.startJVM(
            jvmpath,
            '-Djava.class.path=%s' % classpath,
            '-Dfile.encoding=UTF8',
            '-ea', '-Xmx{}m'.format(max_heap)
        )
    except Exception as e:
        print(e)