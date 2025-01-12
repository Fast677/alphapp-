import { useSession } from '@auth0/nextjs-auth0';

export default function Custom404() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for could not be found.</p>
    </div>
  );
}

