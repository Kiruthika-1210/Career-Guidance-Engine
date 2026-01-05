export default function SummaryCard({ category, summary }) {
  const badgeColor = {
    resume_improvement: "bg-yellow-100 text-yellow-800",
    skill_gap: "bg-red-100 text-red-800",
    career_readiness: "bg-green-100 text-green-800",
  };

  return (
    <div className="mt-6 rounded-xl border bg-white p-5 shadow-sm">
      <div className="flex items-center justify-between mb-3">
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

      <p className="text-gray-700 leading-relaxed">
        {summary}
      </p>
    </div>
  );
}
