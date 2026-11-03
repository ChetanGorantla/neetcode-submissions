class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # compute net distance > 0?
        # do we need sample size of 4 to determine net distance?
        # when can we cut off cycle detection?
        # if we did cycle detection we would have to store r, c, facing
        # let's try 4 step sim

        r = 0
        c = 0
        rdir = 1
        cdir = 0
        for i in range(4):
            for instr in instructions:
                if instr == "G":
                    r+=rdir
                    c+=cdir
                elif instr == "R":
                    # need to make the not operation
                    # make a state machine to see a pattern
                    # (1, 0) -> (0, 1)
                    # (0, 1) -> (-1, 0)
                    # (-1, 0) -> (0, -1)
                    # (0, -1) -> (1, 0)
                    # if cdir == 0 then do regular switch
                    # if rdir == 0 then do negative switch
                    if cdir == 0:
                        rdir, cdir = cdir, rdir
                    else:
                        rdir, cdir = -cdir, -rdir
                elif instr == "L":
                    # assuming it's the opposite? 
                    # (1, 0) -> (0, -1)
                    if rdir == 0:
                        rdir, cdir = cdir, rdir
                    else:
                        rdir, cdir = -cdir, -rdir
        return (r == c == 0 and rdir == 1 and cdir == 0)

