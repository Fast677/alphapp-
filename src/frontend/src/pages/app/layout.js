import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { useUser } from '@auth0/nextjs-auth0';

export default function AppLayout({ children }) {
  const { user, error, isLoading } = useUser();
  const router = useRouter();
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    if (user) {
      // Fetch user role from your backend API
      fetch(`/api/users/${user.sub}`)
        .then((res) => res.json())
        .then((data) => {
          setUserRole(data.role);
        })
        .catch((error) => {
          console.error("Error fetching user role:", error);
          // Handle error appropriately, e.g., redirect to login or show an error message
          router.push('/login');
        });
    }
  }, [user, router]);

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  if (!user) {
    return <p>Please log in.</p>;
  }

  // Restrict access based on user role
  if (userRole !== 'admin' && router.pathname === '/admin') {
    return <p>Access denied.</p>;
  }

  return (
    <div>
      <h1>Welcome, {user.name}!</h1>
      <p>Your role is: {userRole}</p>
      {children}
    </div>
  );
}

