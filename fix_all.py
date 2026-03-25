import os

# Always resolve relative to THIS script's location
ROOT = os.path.dirname(os.path.abspath(__file__))
FRONTEND = os.path.join(ROOT, "frontend")

print(f"Writing files to: {FRONTEND}")

files = {
    os.path.join(FRONTEND, "lib", "api.ts"): '''const BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type Task = {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
};

export type TaskCreate = Omit<Task, "id" | "created_at">;

export const getTasks = () =>
  fetch(`${BASE}/tasks`).then(r => r.json()) as Promise<Task[]>;

export const createTask = (data: TaskCreate) =>
  fetch(`${BASE}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }).then(r => r.json()) as Promise<Task>;

export const updateTask = (id: number, data: TaskCreate) =>
  fetch(`${BASE}/tasks/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }).then(r => r.json()) as Promise<Task>;

export const deleteTask = (id: number) =>
  fetch(`${BASE}/tasks/${id}`, { method: "DELETE" }).then(r => r.json());
''',

    os.path.join(FRONTEND, "app", "page.tsx"): '''"use client";
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
''',

    os.path.join(FRONTEND, "app", "components", "TaskForm.tsx"): '''"use client";
import { useState } from "react";
import { createTask } from "@/lib/api";

export default function TaskForm({ onSaved }: { onSaved: () => void }) {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");

  const submit = async () => {
    if (!title.trim()) return;
    await createTask({ title, description: desc, completed: false });
    setTitle(""); setDesc("");
    onSaved();
  };

  return (
    <div className="bg-white rounded-xl shadow p-4 space-y-3">
      <input
        className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        placeholder="Task title"
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <input
        className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        placeholder="Description (optional)"
        value={desc}
        onChange={e => setDesc(e.target.value)}
      />
      <button
        onClick={submit}
        className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium w-full"
      >
        Add Task
      </button>
    </div>
  );
}
''',

    os.path.join(FRONTEND, "app", "components", "TaskCard.tsx"): '''"use client";
import { Task, updateTask, deleteTask } from "@/lib/api";

export default function TaskCard({ task, onChanged }: { task: Task; onChanged: () => void }) {
  const toggle = async () => {
    await updateTask(task.id, { ...task, completed: !task.completed });
    onChanged();
  };

  const remove = async () => {
    await deleteTask(task.id);
    onChanged();
  };

  return (
    <div className={`bg-white rounded-xl shadow px-4 py-3 flex items-center justify-between ${task.completed ? "opacity-50" : ""}`}>
      <div className="flex items-center gap-3">
        <input type="checkbox" checked={task.completed} onChange={toggle} className="w-4 h-4 cursor-pointer" />
        <div>
          <p className={`font-medium text-sm ${task.completed ? "line-through text-gray-400" : "text-gray-800"}`}>
            {task.title}
          </p>
          {task.description && <p className="text-xs text-gray-400">{task.description}</p>}
        </div>
      </div>
      <button onClick={remove} className="text-red-400 hover:text-red-600 text-xs font-medium">
        Delete
      </button>
    </div>
  );
}
''',

    os.path.join(FRONTEND, ".env.local"): 'NEXT_PUBLIC_API_URL=http://localhost:8000\n',
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {path}")

print("\n🎉 All done!")