# just crop it

## about

Tiny utility to help students help @alexaorrico build out her @holbertonschool project on face verification.

## installation and usage
```sh
git clone git@github.com:egsy/just-crop-it.git
cd just-crop-it
```
Before running program, copy your chosen photos to be cropped into the `original` folder.
```sh
./crop.py

```
✨behold ✨a new folder of square, cropped photos ready to be emailed to alexa


## todo

programmatically implement remainder of alexa's requirements:

- [x] prompt user to input name at commandline and use to label photos
> Please also label these photos as your name in the Intranet followed by an index from 0 to however many photos you have (ex. `AlexaOrrico0.jpg`).

- [x] include check for file extension to be either `jpg` or `png`

- [ ] check size of cropped photo and compress if larger than 2MB
> ...photos of yourself that are *LESS* than 2 MB...

- [ ] send email with cropped photos as attachments upon completion
> please use the subject line `Face Verification`