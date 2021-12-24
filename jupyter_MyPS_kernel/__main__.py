from ipykernel.kernelapp import IPKernelApp
from .kernel import PSKernel
IPKernelApp.launch_instance(kernel_class=PSKernel)
