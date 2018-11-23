## Synthesis/Analysis notebooks for output fro RNNControl

Jupyter notebooks to analyse & visualize RNN models that generate audio synthesis.   

If you just point these analysis files to the output folder for RNNControl, it will always read the most recent parameter file written there and use the last saved model to run the synthesis/analysis code. 

The analysis/visualization all assume 3 control paramters: [instrument, pressure, pitch]

The visualizations include signals, parameters contours, spectra, spectrograms, as well as heatmaps and interactive hidden-layer visualzations (and sonification). 

**Files**  
.  
+--explore_Transients - generates a signal with a square-wave pressure function
+--exploreSweepVolume - generates a volume sweep, ramp up then down
+--exploreSweepPitch - generates a volume sweep, ramp up then down
+--exploreArpeggioPitch - generates a sequence of notes in a major chord, up then down
+--exploreBigFig - generates a bunch of notes and shows signals and spectra
+--exploreLorenz - uses the Lorenz equation to generate wild and crazy parmaeter contours for controling synthesis over time.

+--visualizeHeatAndHidden - just demos visualization techniques
+--loadModelForEvaluation - code common to all the analysis routines (%run from each of them)


**Subdirs**  
* demoModel: pre-trained models and a param file to load for synthesis/analysis 
* utils: 
* output: directory for saving figures from analysis

**Dependencies**  
* pytorch 0.4.0
* RNNControl output (saved models and parameter file) (https://github.com/muhdhuz/RNNControl)
* [audioDataloader](https://github.com/muhdhuz/AudioDataloader)
* [paramManager](https://github.com/lonce/paramManager)
  

**Authors**  
* Lonce Wyse









