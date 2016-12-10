from setuptools import setup

setup(name="fipradio",
      version="1.0",
      author="Alexandre Macabies",
      description="Command line to start & stop the stream and mute unwanted "
                  "songs from FIP radio",
      license="MIT",
      classifiers=["Topic :: Multimedia :: Sound/Audio :: Players",
                   "Environment :: Console",
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3 :: Only"],
      install_requires=['aiohttp'],
      py_modules=['fipradio'],
      scripts=['fip'])