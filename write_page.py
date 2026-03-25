import os

path = os.path.join("frontend", "app", "page.tsx")

content = '''"use client";
import { useEffect, useState } from "react";
import { getTasks, Task } from "@/lib/api";
import TaskForm from "./components/TaskForm";
import TaskCard from "./components/TaskCard";

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);

  const load = () => getTasks().then(setTasks);

  useEffect(() => { load(); }, []);

  return (
    <main className="max-w-2xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">📝 Tasks</h1>
      <TaskForm onSaved={load} />
      <div className="mt-6 space-y-3">
        {tasks.length === 0 && (
          <p className="text-gray-400 text-center mt-10">No tasks yet. Add one above!</p>
        )}
        {tasks.map(t => (
          <TaskCard key={t.id} task={t} onChanged={load} />
        ))}
      </div>
    </main>
  );
}
'''

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Created {path}")