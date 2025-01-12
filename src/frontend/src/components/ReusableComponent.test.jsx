import React from 'react';
import { render } from '@testing-library/react';
import ReusableComponent from './ReusableComponent';

describe('ReusableComponent', () => {
  it('renders children correctly', () => {
    const { getByText } = render(
      <ReusableComponent className="test-class">
        <span>Test Child</span>
      </ReusableComponent>
    );
    expect(getByText('Test Child')).toBeInTheDocument();
  });

  it('applies the given className', () => {
    const { container } = render(
      <ReusableComponent className="test-class">
        <span>Test Child</span>
      </ReusableComponent>
    );
    expect(container.firstChild).toHaveClass('test-class');
  });
});