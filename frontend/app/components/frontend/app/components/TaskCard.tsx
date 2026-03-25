"use client";
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
