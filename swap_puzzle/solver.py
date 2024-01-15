from grid import Grid

class Solver(Grid): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, m, n, initial_state = []):
        super().__init__(m, n, initial_state = [])

    



    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        (m , n) = (len(self.state), len(self.state[0]))
        
        L = []
        for i in range(m):
            L = L + self.state[i]
        A = len(L)
        L_swap = []
        print(L)

        for i in range(A):
            
            if (i+1)%n == 0:
                c_0 = (((i+1)//n)-1, n-1)

            else : 
                c_0 = (((i+1)//n), ((i+1)%n)-1)

            if L[i] != i+1:
                for j in range(i+1, A):
                    if L[j] == i+1:
                        if (j+1)%n == 0:
                            c_1 = (((j+1)//n)-1, n-1)
                        else : 
                            c_1 = (((j+1)//n), ((j+1)%n)-1)
                        L[i], L[j] = L[j], L[i]
                C = (c_0, c_1)
                L_swap.append(C)
        return L_swap


        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

