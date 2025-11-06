from setuptools import setup, find_packages

setup(
    name="port-info-lookup",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["port_info"],  # main module file, e.g., port_info.py
    license="MIT",
    description="A Python utility to fetch and look up network port details using IANA's port assignments",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Md. Ariful Islam",
    author_email="iamx.ariful.islam@gmail.com",
    url="https://github.com/iamx-ariful-islam/port-info-lookup",
    project_urls={
        "Bug Tracker": "https://github.com/iamx-ariful-islam/port-info-lookup/issues",
        "Documentation": "https://github.com/iamx-ariful-islam/port-info-lookup#readme",
        "Source Code": "https://github.com/iamx-ariful-islam/port-info-lookup",
    },
    install_requires=[
        "requests",
    ],
    keywords=[
        "port lookup",
        "network utilities",
        "IANA",
        "tcp",
        "udp",
        "security",
        "iamx-ariful-islam"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules :: Internet",
    ],
    python_requires=">=3.6",
)