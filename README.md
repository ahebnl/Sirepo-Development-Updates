
# Sirepo-Development-Updates
this records the sirepo developments from NSLS-II

### 12, will do : add 'wm_fbk' to script...........

Before running a Sirepo-generated script of NERSC, you should add this option in it:

      ['wm_fbk', '', '1', 'create backup file(s) with propagated multi-e intensity distribution vs horizontal and vertical position and other radiation characteristics', 'store_true'],

By default, this option is not set in the srwl_bl.py file (see https://github.com/ochubar/SRW/blob/master/env/work/srw_python/srwl_bl.py#L3566). 

BTW, I am using now RadiaSoft's Sirepo version for direct simulations at NERSC, in the Debug queue. Great development! I have even prepared a happy slide on this for DOE (see slide #15 in the attached file).
Though this "'wm_fbk " option still has to be added in Sirepo and used there; maybe we can do this and make a pull request to RadiaSoft?.

### 11, the separate tab "Grid Shift" to the "Propagation Parameters" dialog
[example script](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/sxn_v02_250ev_realzp-debug-intensity-watchpoint-56753227m_oc.py)
### ![grid shift](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/propagator_gridshift.PNG)


### 10, the modification of official beamline logo in light-source page
```
https://expdev-test.nsls2.bnl.gov/light#/light-sources
```
### ![light-sources](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/light-sources.PNG)

### 9, "demo videos" is ready to be added
### ![demo_video](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/demo_video.PNG)
[demo_note](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/video-audio-template.txt)

### 8, disable "user register".

### 7, 3D beamline plot generation without wavefront propagation calculation is done; 
### ['op_fno', 's', 'beamline_orient.dat', 'file name for saving orientations of optical elements in the lab frame'] only show for "3D beamline".....

### 6, fixed the following 'Sampling Method' issues in "Intensity, 20m" report:
The issues were reported by Oleg through email: 
1) When I create a new simulation of “Electron Bean with Idealized Undulator”, Sirepo creates a U20 hard X-ray source with NSLS-II e-beam (which is good!). In the “Intensity, 20m” report , in the “pencil” menu, “Main” tab, the “Sampling Method” is by default set to “Automatic”, and “Sampling Factor” set by default to 1. I would like instead the “Sampling Method” to be set to “Manual”, without the “Sampling Factor” shown, and with the “Number of Points vs Position” set to 100 both for the Horizontal and Vertical positions. I note that this default setting should be only changed in the Source mage, and should not affect the default setting in the “Beamline” page (the latter one should remain as is, i.e. set to “Automatic” with “Sampling Factor” = 1 by default)."

2) (Related to the previous, but different issue) Changing between “Sampling Method” “Automatic” and “Manual” setting does not result in disappearing and appearing the “Sampling Factor” and “Number of Points vs Position” input boxes in that dialog, as it should be, according to our logic: i.e. clicking on “Manual” button should make “Sampling Factor” instantly disappear and “Number of Points vs Position” instantly appear, and clicking on “Automatic” button the other way around (as it used to be some time ago, I think).

### 5, fixed the following 'Sampling Method' issues for all example NSLS-II simulations in Sirepo:
The issue was reported by Oleg through email: 
"I think the minor issue of the default intensity calculation method in our example calculations still takes place.
E.g. the CHX’s default dialog from out test server looks like in the attached figure.
I would strongly prefer that instead of Sampling Method -> Automatic and Sampling Factor = 0 it would be by default (on the Source page only!): Sampling Method -> Manual and Numbers of Points vs Position = 100, 100.

BTW, Sampling Factor = 0 switches off the “Automatic” sampling in SRW, so it should not be used by default even with the Sampling Method -> Automatic (we can use our nominal default value Sampling Factor = 1 when one would try to set Sampling Method -> Automatic first time)."

"It can be fixed by modifying these examples’ json files one by one. 
Before I do the fixing, I need confirm that ‘Sampling Method -> Manual and Numbers of Points vs Position = 100, 100’ is for all these default examples. Right?
" by An's reply

### 4, fixed the issue with initial conditions for e- trajectory for all examples.
this issue was reported by Oleg through email:
"We were observing some strange behaviors of recent versions of Sirepo related to setting initial conditions for calculating electron trajectory and all other dependent calculations. 
I am attaching a zip-file generated on our simulation server at NSLS-II (https://expdev.nsls2.bnl.gov/, inside BNL firewall). I tried to import this simulation file to https://www.sirepo.com/srw#/simulations, and had an issue that the electron trajectory gets “tilted”, and all subsequent results become wrong. This happens because on our server, the initial conditions for the trajectory are specified “automatically” before undulator (at -1.54 m long. pos.), whereas after the import to https://www.sirepo.com/, they appear to be set at zero long. pos., i.e. in the middle of undulator......"

The correct values should be ‘Manual’ and ‘-1.8’.
### ![ebeam_initial](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/ebeam_initial.PNG)

### 3, fixed some issue in the field of 'degree of coherence'.

### 2, For grating, there are following updating:
* add “Compute Parameters from”, then when input ‘energy’ and ‘cff’ (or ‘grazing angle’), it will automatically calculate ‘grazing angle’ (or ‘cff’).
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Height Profile' to grating field.

### 1, For crystal, there are following updating:
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Height Profile' to grating field.
