# Shopify-Challenge---Image-Repo

A SQLite-based python image repository with auto-tagging.

Based on the Shopify 2021 Intern Challenge
https://docs.google.com/document/d/1ZKRywXQLZWOqVOHC4JkF3LqdpO3Llpfk_CkZPR8bjak/edit#heading=h.n7bww7g70ipk

# Implementation details / Use

An empty repository is included in the source files, but to recreate it, simply run db_setup.py

Images that are added to the repository are automatically tagged using Yolov3 and the COCO database, and are given a list of tags based on the items detected in the image.
New images can also include a string with metadata, which will be stored alongside them in the repository.
For more information about creating new images, see the constructor in myImage.py

Repository access is detailed in db_funcs.py, and includes:
Adding new images/Removing new images by their unique id (filename)
Image search by tag, which returns the ids of all images with the given items in them.
Image retrieval by id, which returns the PIL image object for an item with the given id.
