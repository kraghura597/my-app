const BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

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
