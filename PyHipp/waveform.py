import DataProcessingTools as DPT
import matplotlib.pyplot as plt
<<<<<<< HEAD
import hickle as hkl
import os
import numpy as np
<<<<<<< HEAD
=======
import os
import hickle as hkl
import numpy as np
from .misc import getChannelInArray
>>>>>>> upstream/master
=======
from .misc import getChannelInArray
>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10

class Waveform(DPT.DPObject):
    # Please change the class name according to your needs
    filename = 'waveform.hkl'  # this is the filename that will be saved if it's run with saveLevel=1
<<<<<<< HEAD
    argsList = []  # these is where arguments used in the creation of the object are listed
=======
    argsList = [("mountainsDirectory", "mountains"), 
        ("ouputDirectory","output"), ("templateFilename","templates.hkl")]
>>>>>>> upstream/master
    level = 'channel'  # this is the level that this object will be created in

    def __init__(self, *args, **kwargs):
        DPT.DPObject.__init__(self, *args, **kwargs)

    def create(self, *args, **kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
        # this function will be called once to create this waveform object
=======
        # thie function will be called by PanGUI.main once to create this waveform object
>>>>>>> upstream/master
        
        # one neat property of Object-Oriented Programming (OOP) structure is that 
        # you can create some field-value pairs that can be called and updated 
        # in all functions of the object, if you specify the function properly.
        # The only thing that you need to do is to instantiate those fields in
        # this function with the prefix 'self.', then you can call them and 
        # edit them in all the other functions that have the first input argument
        # being 'self'
        #
        # For exmample, if you instantiate a field-value pair:
        # self.name = IronMan
        #
        # You can then call them or edit them in other functions:
        # def get_name(self):
        #    print(self.name)
        #
        # def set_name(self, new_name):
        #    self.name = new_name
        #
        # In this way, you don't need to return and pass in so many arguments 
        # across different functions anymore :)
        
<<<<<<< HEAD
        
        # The following is some hints of the things-to-do:
        
        # read the mountainsort template files
        # .........................................
        # ..................code...................
        # .........................................
=======
>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
        pwd = os.path.normpath(os.getcwd())
        # 'channelxxx, xxx is the number of the channel'
        self.channel_filename = [os.path.basename(pwd)]
        template_filename = os.path.join(DPT.levels.resolve_level('day', self.channel_filename[0]),'mountains', self.channel_filename[0], 'output', 'templates.hkl')
        templates = hkl.load(template_filename)
        self.data = [np.squeeze(templates)]
        aname = DPT.levels.normpath(os.path.dirname(pwd))
        self.array_dict = dict()
        self.array_dict[aname] = 0
        self.numSets = 1
        self.current_plot_type = None

        # check on the mountainsort template data and create a DPT object accordingly
        # Example:
        if (len(self.data)):
            # create object if data is not empty
=======
        # The following is some hints of the things-to-do:
        # get current channel name
        pwd = os.path.normpath(os.getcwd());
        self.channel_filename = [os.path.basename(pwd)]  # 'channelxxx, xxx is the number of the channel'
        self.read_templates()  # read the mountainsort template files
        
        # check on the mountainsort template data and create a DPT object accordingly
        if self.data[0].all():
            # create object if data is not empty
            self.numSets = 1
            # get array name
            aname = DPT.levels.normpath(os.path.dirname(pwd))
            self.array_dict = dict()
            self.array_dict[aname] = 0
            self.current_plot_type = None
>>>>>>> upstream/master
            DPT.DPObject.create(self, *args, **kwargs)
        else:
            # create empty object if data is empty
            DPT.DPObject.create(self, dirs=[], *args, **kwargs)            
<<<<<<< HEAD
        
=======

>>>>>>> upstream/master
    def append(self, wf):
        # this function will be called by processDirs to append the values of certain fields
        # from an extra object (wf) to this object
        # It is useful to store the information of the objects for panning through in the future
        DPT.DPObject.append(self, wf)  # append self.setidx and self.dirs
<<<<<<< HEAD
        # .........................................
        # ..................code...................
        # .........................................
        self.data = self.data + wf.data
        for ar in wf.array_dict:
            self.array_dict[ar] = self.numSets
        self.numSets += 1
<<<<<<< HEAD


=======
        self.data += wf.data
        # loop through array dictionary in wf
        for ar in wf.array_dict:
            self.array_dict[ar] = self.numSets
        self.numSets += 1
>>>>>>> upstream/master
        
=======
     
>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
    def plot(self, i = None, ax = None, getNumEvents = False, getLevels = False,\
             getPlotOpts = False, overlay = False, **kwargs):
        plotOpts = {'PlotType': DPT.objects.ExclusiveOptions(['Channel', 'Array'], 0), \
<<<<<<< HEAD
            'LabelsOff': False, 'TitleOff': False}
=======
            'LabelsOff': False, 'TitleOff': False, 'TicksOff': False}
>>>>>>> upstream/master

        # update the plotOpts based on kwargs, these two lines are important to
        # receive the input arguments and act accordingly
        for (k, v) in plotOpts.items():
                    plotOpts[k] = kwargs.get(k, v)  
                    
<<<<<<< HEAD
        plot_type = plotOpts['PlotType'].selected()  # this variable will store the selected item in 'Type'

        if getPlotOpts:  # this will be called by PanGUI.main to obtain the plotOpts to create a menu once we right-click on the axis
            return plotOpts 

<<<<<<< HEAD
=======
        if getPlotOpts:  # this will be called by PanGUI.main to obtain the plotOpts to create a menu once we right-click on the axis
            return plotOpts 

        plot_type = plotOpts['PlotType'].selected()  # this variable will store the selected item in 'Type'

        if self.current_plot_type is None:  # initial assignement of self.current_plot_type
            self.current_plot_type = plot_type

>>>>>>> upstream/master
=======
        if self.current_plot_type is None:
            self.current_plot_type = plot_type

>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
        if getNumEvents:  
            # this will be called by PanGUI.main to return two values: 
            # first value is the total number of items to pan through, 
            # second value is the current index of the item to plot
<<<<<<< HEAD
            # .........................................
            # ..................code...................
            # .........................................
            if self.current_plot_type == plot_type:
                if plot_type == 'Channel':
                    return self.numSets, i
                elif plot_type == 'Array':
                    return len(self.array_dict), self.array_dict[i]
            
<<<<<<< HEAD
            return  # please return two items here: <total-number-of-items-to-plot>, <current-item-index-to-plot>
=======
            if self.current_plot_type == plot_type:  # no changes to plot_type
                if plot_type == 'Channel':
                    return self.numSets, i
                elif plot_type == 'Array':
                    return len(self.array_dict), i
            elif self.current_plot_type == 'Array' and plot_type == 'Channel':  # change from array to channel
                if i == 0:
                    return self.numSets, 0
                else:
                    # get values in array_dict
                    advals = np.array([*self.array_dict.values()])
                    return self.numSets, advals[i-1]+1
            elif self.current_plot_type == 'Channel' and plot_type == 'Array':  # change from array to channel
                # get values in array_dict
                advals = np.array([*self.array_dict.values()])
                # find index that is larger than i
                vi = (advals >= i).nonzero()
                return len(self.array_dict), vi[0][0]
>>>>>>> upstream/master
                
=======
            elif self.current_plot_type == 'Array' and plot_type == 'Channel':
                # add code to return number of channels and the appropriate
                # channel number if the current array number is i
                for pos,value in enumerate(self.array_dict.values()):
                    if(i==0):
                        return len(self.dirs),0
                    elif(pos==i):
                        return len(self.dirs),value
            elif self.current_plot_type == 'Channel' and plot_type == 'Array':
                # add code to return number of arrays and the appropriate
                # array number if the current channel number is i
                self.current_plot_type = 'Array'
                for pos,value in enumerate(self.array_dict.values()):
                    if(i<=value):
                        return len(self.array_dict),pos

>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
        if ax is None:
            ax = plt.gca()

        if not overlay:
            ax.clear()
        
        ######################################################################
        #################### start plotting ##################################
        ######################################################################
        fig = ax.figure # get the parent figure of the ax

        if plot_type == 'Channel':  # plot in channel level
<<<<<<< HEAD
<<<<<<< HEAD
            # plot the mountainsort data according to the current index 'i'
            # .........................................
            # ..................code...................
            # .........................................
            pass  # you may delete this line
    
        ########labels###############
        if not plotOpts['TitleOff']:  # if TitleOff icon in the right-click menu is clicked
            # set the title in this format: channelxxx, fill with zeros if the channel number is not three-digit
            # .........................................
            # ..................codes..................
            # .........................................
            pass  # you may delete this line
=======
            if self.current_plot_type == 'Array':
                self.remove_subplots(fig)
                ax = fig.add_subplot(1,1,1)

            self.plot_data(i, ax, plotOpts, 1)
            self.current_plot_type = 'Channel'

        elif plot_type == 'Array':
            self.remove_subplots(fig)
            advals = np.array([*self.array_dict.values()])

            if(i==0):
                cstart = 0
                cend = advals[0]
>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
            
            else:
                cstart = advals[i-1] + 1
                cend = advals[i]
        
            # set the ending index cend for array i
            currch = cstart
            while currch <= cend :
                # get channel name
                currchname = self.dirs[currch]
                # get axis position for channel
                ax, isCorner = getChannelInArray(currchname, fig)
                self.plot_data(currch, ax, plotOpts, isCorner)
                currch += 1
            self.current_plot_type = 'Array'
            
        return ax
    
<<<<<<< HEAD
    
=======
            if self.current_plot_type == 'Array':
                fig = ax.figure  # get the parent figure of the ax
                for x in fig.get_axes():  # remove all axes in current figure
                    x.remove()    
                ax = fig.add_subplot(1,1,1)
                
            # plot the mountainsort data according to the current index 'i'
            self.plot_data(i, ax, plotOpts, 1)
            self.current_plot_type = 'Channel'
                    
        elif plot_type == 'Array':  # plot in channel level
            fig = ax.figure  # get the parent figure of the ax
            for x in fig.get_axes():  # remove all axes in current figure
                x.remove()    

            # get values in array_dict
            advals = np.array([*self.array_dict.values()])
            # get first channel, which will be the last index in the previous array plus 1
            if i == 0:
                cstart = 0
                cend = advals[0]
            else:
                cstart = advals[i-1] + 1
                cend = advals[i]
            
            currch = cstart
            plotOpts['LabelsOff'] = True
            plotOpts['TitleOff'] = True
            plotOpts['TicksOff'] = True
            while currch <= cend :
                # get channel name
                currchname = self.dirs[currch]
                # get axis position for channel
                ax,isCorner = getChannelInArray(currchname, fig)
                self.plot_data(currch, ax, plotOpts, isCorner)
                currch += 1
                
            self.current_plot_type = 'Array'
>>>>>>> upstream/master
=======
    def plot_data(self, i, ax, plotOpts, isCorner):
        y = self.data[i]
        x = np.arange(y.shape[0])
        ax.plot(x, y)
        
        if not plotOpts['TitleOff']:
            ax.set_title(self.dirs[i])
        
        if (not plotOpts['LabelsOff']) or isCorner:
            ax.set_xlabel('Time (sample unit)')
            ax.set_ylabel('Voltage (uV)')

    def remove_subplots(self, fig):
        for x in fig.get_axes(): # remove all axes in current figure
            x.remove()

>>>>>>> 8d350ff78a1786fab8f444ae40e9d957cec8bd10
    
    #%% helper functions        
    # Please make use of the properties of the OOP to call and edit the field-value
    # pairs that can be shared across different functions in this object.
    # This will greatly increase the efficiency in maintaining the codes,
    # especially for those lines that are used for multiple times in multiple places.
    # Other than that, this will also greatly increase the readability of the code
<<<<<<< HEAD
        
        
    
=======
    def read_templates(self):
        # make the following items as lists for the sake of self.append
        template_fileanme = os.path.join(DPT.levels.resolve_level("day", self.channel_filename[0]),
                                         self.args["mountainsDirectory"],
                                         self.channel_filename[0],
                                         self.args["ouputDirectory"],
                                         self.args["templateFilename"])
        if os.path.isfile(template_fileanme):
            self.data = [np.squeeze(hkl.load(template_fileanme))]
        else:
            print('No mountainsort template file was found for {0}...'.format(self.channel_filename[0]))
            self.data = [np.array([])]
        
    def plot_data(self, ind, ax, plotOpts, isCorner):
        # plot the mountainsort data according to the index 'ind'
        y = self.data[ind]
        x = np.arange(y.shape[0])
        ax.plot(x, y)

        ########labels###############
        if not plotOpts['TitleOff']:  # if TitleOff icon in the right-click menu is clicked
            ax.set_title(self.dirs[ind])
                
        if (not plotOpts['LabelsOff']) or isCorner:  # if LabelsOff icon in the right-click menu is clicked
            ax.set_xlabel('Time (sample unit)')
            ax.set_ylabel('Voltage (uV)')
            
        if plotOpts['TicksOff'] or (not isCorner):
            ax.set_xticks([])
            ax.set_yticks([])
>>>>>>> upstream/master
