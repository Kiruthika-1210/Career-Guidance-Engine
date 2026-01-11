export default function SummaryCard({ category, summary, roadmap, score }) {
  const badgeColor = {
    resume_improvement: "bg-yellow-100 text-yellow-800",
    skill_gap: "bg-red-100 text-red-800",
    career_readiness: "bg-green-100 text-green-800",
  };

  return (
    <div className="mt-6 rounded-xl border bg-white p-5 shadow-sm space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold text-gray-800">
          Career Guidance Summary
        </h2>

        {category && (
          <span
            className={`px-3 py-1 rounded-full text-xs font-medium ${
              badgeColor[category]
            }`}
          >
            {category.replace("_", " ")}
          </span>
        )}
      </div>

      {score !== null && (
        <p className="text-sm text-gray-600">
          Career Readiness Score: <b>{score} / 5</b>
        </p>
      )}

      <p className="text-gray-700 leading-relaxed">{summary}</p>

      {roadmap && (
        <div className="mt-4">
          <h3 className="font-semibold text-gray-800 mb-2">
            Recommended Roadmap
          </h3>
          <ul className="list-disc ml-5 space-y-1 text-gray-700 text-sm">
            <li><b>30 Days:</b> {roadmap["30_days"]}</li>
            <li><b>60 Days:</b> {roadmap["60_days"]}</li>
            <li><b>90 Days:</b> {roadmap["90_days"]}</li>
          </ul>
        </div>
      )}
    </div>
  );
}
