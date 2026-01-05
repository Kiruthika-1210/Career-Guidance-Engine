from langgraph.graph import StateGraph
from .state import CareerState
from .nodes import (
    start_node,
    router_node,
    resume_improvement_node,
    skill_gap_node,
    career_readiness_node,
    end_node,
)

def build_graph():
    graph = StateGraph(CareerState)

    graph.add_node("start", start_node)
    graph.add_node("router", router_node)
    graph.add_node("resume_improvement", resume_improvement_node)
    graph.add_node("skill_gap", skill_gap_node)
    graph.add_node("career_readiness", career_readiness_node)
    graph.add_node("end", end_node)

    graph.set_entry_point("start")

    # ✅ FIXED CONDITIONAL EDGE
    graph.add_conditional_edges(
        "start",
        lambda state: "proceed" if state.get("final_reply") is None else "stop",
        {
            "proceed": "router",
            "stop": "end",
        },
    )

    graph.add_conditional_edges(
        "router",
        lambda state: state["guidance_category"],
        {
            "resume_improvement": "resume_improvement",
            "skill_gap": "skill_gap",
            "career_readiness": "career_readiness",
        },
    )

    graph.add_edge("resume_improvement", "end")
    graph.add_edge("skill_gap", "end")
    graph.add_edge("career_readiness", "end")

    return graph.compile()
