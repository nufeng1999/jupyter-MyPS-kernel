from setuptools import setup

setup(name='jupyter_MyPS_kernel',
      version='0.0.1',
      description='Minimalistic PowerShell kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyPS-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyPS-kernel/tarball/0.0.1',
      packages=['jupyter_MyPS_kernel'],
      scripts=['jupyter_MyPS_kernel/install_MyPS_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'shell','powershell','ps','ps2'],
      include_package_data=True
      )
