import { useSession } from '@auth0/nextjs-auth0';

export default function Terms() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Terms</h1>
      <p>This is the terms page.</p>
    </div>
  );
}

