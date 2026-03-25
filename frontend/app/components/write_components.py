import os

base = os.path.join("frontend", "app", "components")
os.makedirs(base, exist_ok=True)

# TaskForm.tsx
with open(os.path.join(base, "TaskForm.tsx"), "w", encoding="utf-8") as f:
    f.write('''"use client";
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
''')
print("✅ Created TaskForm.tsx")

# TaskCard.tsx
with open(os.path.join(base, "TaskCard.tsx"), "w", encoding="utf-8") as f:
    f.write('''"use client";
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
''')
print("✅ Created TaskCard.tsx")

# Also write lib/api.ts
lib_path = os.path.join("frontend", "lib")
os.makedirs(lib_path, exist_ok=True)
with open(os.path.join(lib_path, "api.ts"), "w", encoding="utf-8") as f:
    f.write('''const BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

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
''')
print("✅ Created lib/api.ts")

print("\n🎉 All done! Restart your frontend.")