from langgraph.graph import StateGraph
from .state import CareerState
from .nodes import *

def build_graph():
    graph = StateGraph(CareerState)

    graph.add_node("start", start_node)
    graph.add_node("router", router_node)
    graph.add_node("follow_up", follow_up_node)
    graph.add_node("skill_gap", skill_gap_node)
    graph.add_node("resume_improvement", resume_improvement_node)
    graph.add_node("career_readiness", career_readiness_node)
    graph.add_node("end", end_node)

    graph.set_entry_point("start")

    graph.add_edge("start", "router")

    graph.add_conditional_edges(
    "router",
    lambda state: state["guidance_category"],
    {
        "follow_up": "follow_up",
        "resume_improvement": "resume_improvement",  # ✅ FIX
        "skill_gap": "skill_gap",
        "career_readiness": "career_readiness",
    },
    )

    graph.add_edge("follow_up", "end")
    graph.add_edge("skill_gap", "end")
    graph.add_edge("resume_improvement", "end")
    graph.add_edge("career_readiness", "end")

    return graph.compile()
