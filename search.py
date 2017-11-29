# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    lijstje = []
    starttuple = (problem.getStartState(), [], 0)
    stack = util.Stack()
    stack.push(starttuple)

    while not stack.isEmpty():
        firstelement = stack.pop()
        pos = firstelement[0]
        if pos in lijstje:
            continue
        if problem.isGoalState(pos):
            break
        lijstje.append(pos)
        for suc in problem.getSuccessors(pos):
            if not suc[0] in lijstje:
                newdir = suc[1]
                newtuple = (suc[0], firstelement[1] + [newdir], suc[2])
                stack.push(newtuple)
    return firstelement[1]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    beenhere = []
    parents = dict()
    starttuple = (problem.getStartState(), 'None', 1)
    stack = util.Queue()
    stack.push(starttuple)

    while not stack.isEmpty():
        firstelement = stack.pop()
        pos = firstelement[0]
        if pos in beenhere:
            continue
        if problem.isGoalState(pos):
            break
        beenhere.append(pos)
        for suc in problem.getSuccessors(pos):
            if not suc[0] in beenhere:
                parents[suc] = firstelement
                stack.push(suc)

    movements = []
    lastpos = firstelement
    while not lastpos[1] == 'None':
        movements.append(lastpos[1])
        lastpos = parents[lastpos]

    movements.reverse()
    return movements

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    beenhere = []
    parents = dict()
    cost = 0
    starttuple = (problem.getStartState(), 'None', 0)
    stack = util.PriorityQueue()
    stack.push(starttuple, cost)

    while not stack.isEmpty():
        firstelement = stack.pop()
        pos = firstelement[0]
        cost = firstelement[2]
        if pos in beenhere:
            continue
        if problem.isGoalState(pos):
            break
        beenhere.append(pos)
        for suc in problem.getSuccessors(pos):
            if not suc[0] in beenhere:
                parents[(suc[0], suc[1])] = (firstelement[0], firstelement[1])
                newtuple = (suc[0], suc[1], suc[2] + cost)
                stack.push(newtuple, newtuple[2])

    movements = []
    lastpos = (firstelement[0], firstelement[1])
    while not lastpos[1] == 'None':
        movements.append(lastpos[1])
        lastpos = parents[lastpos]

    movements.reverse()
    return movements

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
