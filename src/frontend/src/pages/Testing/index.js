import { useSession } from '@auth0/nextjs-auth0';

export default function Testing() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Testing</h1>
      <p>This is the testing page.</p>
    </div>
  );
}

