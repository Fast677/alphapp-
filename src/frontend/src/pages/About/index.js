import { useUser } from '@auth0/nextjs-auth0';

export default function About() {
  const { user, error, isLoading } = useUser();

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  if (!user) {
    return <p>Please log in.</p>;
  }

  return (
    <div>
      <h1>Welcome to About, {user.name}!</h1>
      <p>This is the about page.</p>
    </div>
  );
}

