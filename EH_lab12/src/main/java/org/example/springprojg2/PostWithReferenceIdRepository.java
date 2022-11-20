package org.example.springprojg2;

import org.springframework.data.jpa.repository.JpaRepository;

public interface PostWithReferenceIdRepository extends JpaRepository<PostWithReferenceId, Long> {
}
