import { useSession } from '@auth0/nextjs-auth0';

export default function Resources() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Resources</h1>
      <p>This is the resources page.</p>
    </div>
  );
}

