"""
This module provides an Experiment class which serves as the main interface to process
data and run subsequent analyses.
"""


import os

from pixels.session import Session, get_sessions


class Experiment:
    def __init__(self, mouse_ids, data_dir, meta_dir):
        if not isinstance(mouse_ids, (list, tuple, set)):
            mouse_ids = [mouse_ids]

        self.mouse_ids = mouse_ids
        self.data_dir = os.path.expanduser(data_dir)
        self.meta_dir = os.path.expanduser(meta_dir)
        self.sessions = get_sessions(mouse_ids, self.data_dir, self.meta_dir)

    def extract_spikes(self, resample=True):
        """
        Extract the spikes from raw spike data for all sessions.
        """
        for session in self.sessions:
            session.extract_spikes(resample=resample)

    def process_lfp(self, resample=True):
        """
        Process the LFP data from the raw neural recording data for all sessions.
        """
        for session in self.sessions:
            session.process_lfp(resample=resample)

    def process_behaviour(self):
        """
        Process behavioural data from raw tdms files for all sessions.
        """
        for session in self.sessions:
            session.process_behaviour()

    def process_motion_tracking(self):
        """
        Process motion tracking data either from raw camera data, or from
        previously-generated deeplabcut coordinate data, for all sessions.
        """
        for session in self.sessions:
            session.process_motion_tracking()