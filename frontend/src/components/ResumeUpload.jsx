export default function ResumeUpload() {
  return (
    <div className="flex flex-col gap-2">
      <label className="text-sm font-medium text-gray-700">
        Upload Resume (PDF)
      </label>

      <input
        type="file"
        accept=".pdf"
        name="resume"
        className="block w-full text-sm
                   file:mr-4 file:py-2 file:px-4
                   file:rounded-md file:border-0
                   file:text-sm file:font-semibold
                   file:bg-blue-50 file:text-blue-700
                   hover:file:bg-blue-100"
      />
    </div>
  );
}
