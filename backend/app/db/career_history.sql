CREATE TABLE IF NOT EXISTS career_history (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,

  career_goal TEXT NOT NULL,
  experience_level TEXT NOT NULL,

  guidance_category TEXT NOT NULL,
  score INTEGER NOT NULL,

  gaps TEXT[],
  roadmap JSONB,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Optional but recommended indexes
CREATE INDEX IF NOT EXISTS idx_career_history_created_at
ON career_history (created_at);

CREATE INDEX IF NOT EXISTS idx_career_history_category
ON career_history (guidance_category);
