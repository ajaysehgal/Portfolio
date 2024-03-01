import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/todos')
      .then(res => {
        setTodos(res.data);
      })
      .catch(err => console.log(err));
  }, []);

  const addTodo = () => {
    axios.post('http://localhost:5000/todos', { task, completed: false })
      .then(res => {
        setTodos([...todos, res.data]);
        setTask('');
      })
      .catch(err => console.log(err));
  };

  const toggleTodo = (id, completed) => {
    axios.put(`http://localhost:5000/todos/${id}`, { completed: !completed })
      .then(res => {
        const updatedTodos = todos.map(todo => {
          if (todo._id === id) {
            return { ...todo, completed: !completed };
          }
          return todo;
        });
        setTodos(updatedTodos);
      })
      .catch(err => console.log(err));
  };

  const deleteTodo = (id) => {
    axios.delete(`http://localhost:5000/todos/${id}`)
      .then(res => {
        const updatedTodos = todos.filter(todo => todo._id !== id);
        setTodos(updatedTodos);
      })
      .catch(err => console.log(err));
  };

  return (
    <div>
      <h1>Todo List</h1>
      <input type="text" value={task} onChange={(e) => setTask(e.target.value)} />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map(todo => (
          <li key={todo._id}>
            <input type="checkbox" checked={todo.completed} onChange={() => toggleTodo(todo._id, todo.completed)} />
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>{todo.task}</span>
            <button onClick={() => deleteTodo(todo._id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
