from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      author='Rodion Tiutiunyk',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
