"use client";
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
