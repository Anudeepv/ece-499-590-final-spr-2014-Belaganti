#!/usr/bin/env python
import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()
# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()



	# Get the current feed-forward (state) 


	# Print out the actual position of the LEB
#knees bend
ref.ref[RHP]=0.2
ref.ref[LHP]=0.2
ref.ref[RKN]=0.2
ref.ref[LKN]=0.2
r.put(ref)
time.sleep(1)
#lift left leg
ref.ref[RKN]=0.4
r.put(ref)
# Close the connection to the channels
r.close()
s.close()
