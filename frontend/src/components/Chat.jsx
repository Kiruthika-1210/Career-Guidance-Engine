import { useState } from "react";
import { sendChat } from "../api";
import ResumeUpload from "./ResumeUpload";
import SummaryCard from "./SummaryCard";

export default function Chat() {
  const [reply, setReply] = useState("");
  const [category, setCategory] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    try {
      const formData = new FormData(e.target); // resume included automatically
      const res = await sendChat(formData);    // ✅ await INSIDE async

      setReply(res.reply);
      setCategory(res.guidance_category || null);
    } catch (err) {
      setReply("Error connecting to server.");
      setCategory(null);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-xl mx-auto">
      <form
        onSubmit={handleSubmit}
        className="space-y-4 bg-gray-50 p-5 rounded-xl"
      >
        <input
          name="career_goal"
          placeholder="Target Role (e.g. Software Engineer)"
          className="input"
        />

        <input
          name="experience_level"
          placeholder="Experience Level (student / fresher / early-career)"
          className="input"
        />

        <ResumeUpload />

        <button type="submit" className="btn w-full">
          {loading ? "Analyzing..." : "Send"}
        </button>
      </form>

      {reply && (
        <SummaryCard
          summary={reply}
          category={category}
        />
      )}
    </div>
  );
}
