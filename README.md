
'''
The MyCanny implmentation uses a complex Scharr operator, and thus returns a complex 2dArray
aka, it does not return an array that can be shown as an image
using the np.angle function turns the complex array into a real one but it looks like either 
something is happening to the original img (not the file but the variable) or the angle are 
exploding and the grayscalling has a relative implementation and is exploding because of it
'''

# LineAnalyzer
I am learning to draw, end goal of this project is to have rigours measures of my progress. We'll see.

## TODO (in no particular order) 
### For ghosting exercise
1. Feature detection for dots and lines
2. color match corresponding dots and lines post dectection
3. Dotted draw perfect line between points
4. Compare "perfect" to drawn lines w/ linear functional to obtain preformance measure
5. Second measure in line terminals and position of guiding dots
6. Implement error in pixel measurements

#### Feature Detection for Dots and lines


The MyCanny implmentation uses a complex Scharr operator, and thus returns a complex 2dArray
aka, it does not return an array that can be shown as an image
using the np.angle function turns the complex array into a real one but it looks like either 
something is happening to the original img (not the file but the variable) or the angle are 
exploding and the grayscalling has a relative implementation and is exploding because of it

