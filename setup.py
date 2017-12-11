from distutils.core import setup
# from setuptools import setup

setup(name="envkey",
      version="1.0.0",
      description="EnvKey's python library. Protect API keys and credentials. Keep configuration in sync.",
      url="https://github.com/envkey/envkey-python",
      keywords=["security", "secrets management", "configuration management", "environment variables", "configuration", "python"],
      author="EnvKey",
      author_email="support@nvkey.com",
      license="MIT",
      packages=["envkey"],
      package_data={"envkey": ["ext/**/*"]},
      install_requires=["python-dotenv>=0.7.1"],
      download_url = 'https://github.com/envkey/envkey-python/archive/1.0.0.tar.gz',
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
      ],
      zip_safe=False)