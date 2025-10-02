from setuptools import setup

setup(
    name="kolibri_chat_room",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A basic chat room plugin for Kolibri",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kolibri_chat_room",
    packages=["chat_room"],
    include_package_data=True,
    install_requires=["kolibri>=0.16.0"],  # Adjust to your Kolibri version
    zip_safe=False,
    entry_points={
        "kolibri.plugin": [
            "chat_room = chat_room.kolibri_plugin:ChatRoomPlugin",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)