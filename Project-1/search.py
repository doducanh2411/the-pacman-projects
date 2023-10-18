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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    if (problem.isGoalState(problem.getStartState())):
        return []

    path = []
    visited = []
    queue = Queue()
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        v, path = queue.pop()

        if v in visited:
            continue

        visited.append(v)

        if problem.isGoalState(v):
            return path

        for successor in problem.getSuccessors(v):
            next_state, action, _ = successor  

            if next_state not in visited:
                queue.push((next_state, path + [action]))

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    # startState = problem.getStartState()
    # g = { startState: 0 }
    # f = g[startState] + heuristic(startState, problem)

    # states = PriorityQueue()
    # states.push(startState, f)

    # actions = { startState: [] }

    # while (True):
    #     if states.isEmpty():
    #         return
        
    #     expandedState = states.pop()
    #     expandedActions = actions[expandedState]

    #     if problem.isGoalState(expandedState):
    #         return expandedActions
        
    #     for (successorState, action, _) in problem.getSuccessors(expandedState):
    #         tmp_g = g[expandedState] + problem.getCostOfActions([action])
    #         if successorState in g and g[successorState] < tmp_g:
    #             continue

    #         g[successorState] = tmp_g
    #         f = g[successorState] + heuristic(successorState, problem)

    #         states.update(successorState, f)

    #         actions[successorState] = expandedActions + [action]

    startState = problem.getStartState()

    openStates = PriorityQueue()
    openStates.push(startState, 0)

    g = { startState: 0 }

    path = { startState: [] }

    while (True):
        if openStates.isEmpty():
            return
        
        currentState = openStates.pop()

        if problem.isGoalState(currentState):
            return path[currentState]

        for (successorState, action, _) in problem.getSuccessors(currentState):
            tmp_currentState_g = g[currentState] + problem.getCostOfActions([action])
            if successorState not in g or tmp_currentState_g < g[currentState]:
                g[successorState] = tmp_currentState_g

                f = tmp_currentState_g + heuristic(currentState, problem)
                openStates.update(successorState, f)

                path[successorState] = path[currentState] + [action]

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch