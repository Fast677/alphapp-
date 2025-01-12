import { useSession } from '@auth0/nextjs-auth0';

export default function ErrorPage({ error }) {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Error</h1>
      <p>An error occurred: {error.message}</p>
    </div>
  );
}

